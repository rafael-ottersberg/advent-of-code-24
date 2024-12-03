add_library( day04 day04.cpp)

target_include_directories(day04 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day04 TBB::tbb )