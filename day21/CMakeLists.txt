add_library( day21 day21.cpp)

target_include_directories(day21 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day21 TBB::tbb )