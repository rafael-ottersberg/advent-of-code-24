add_library( day18 day18.cpp)

target_include_directories(day18 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day18 TBB::tbb )